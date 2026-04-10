/// Magic header for precompiled automaton blobs.
///
/// Format (28 bytes, all little-endian):
///   [0..8]   magic          = b"ZHTWDAAC"
///   [8..10]  header_version : u16 (currently 1)
///   [10..14] daachorse_ver  : u32 packed as (major<<16 | minor<<8 | patch)
///   [14..22] dict_hash      : [u8; 8]  (first 8 bytes of blake3)
///   [22]     source_mask    : u8  (bit 0 = Cn, bit 1 = Hk)
///   [23..28] reserved       : [u8; 5]  (MBZ)

pub(crate) const ZHTW_AUTOMATON_MAGIC: [u8; 8] = *b"ZHTWDAAC";
pub(crate) const CURRENT_HEADER_VERSION: u16 = 1;
pub(crate) const HEADER_LEN: usize = 28;
pub(crate) const DAACHORSE_VERSION_PACKED: u32 = 0x0001_0000; // 1.0.0

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub(crate) struct SourceMask(pub u8);

impl SourceMask {
    pub const CN: Self = SourceMask(0b01);
    pub const HK: Self = SourceMask(0b10);
    pub const CN_HK: Self = SourceMask(0b11);
}

impl std::ops::BitOr for SourceMask {
    type Output = Self;
    fn bitor(self, rhs: Self) -> Self {
        SourceMask(self.0 | rhs.0)
    }
}

/// Build a 28-byte header.
pub(crate) fn build_header(dict_hash: [u8; 8], source_mask: SourceMask) -> [u8; HEADER_LEN] {
    let mut buf = [0u8; HEADER_LEN];
    buf[0..8].copy_from_slice(&ZHTW_AUTOMATON_MAGIC);
    buf[8..10].copy_from_slice(&CURRENT_HEADER_VERSION.to_le_bytes());
    buf[10..14].copy_from_slice(&DAACHORSE_VERSION_PACKED.to_le_bytes());
    buf[14..22].copy_from_slice(&dict_hash);
    buf[22] = source_mask.0;
    buf
}

/// Verify header and return payload slice. Panics on mismatch.
pub(crate) fn verify_header(bytes: &[u8], expected: SourceMask) -> &[u8] {
    if bytes.len() < HEADER_LEN {
        panic!(
            "zhtw: automaton bytes truncated (got {} bytes, need >= {})",
            bytes.len(),
            HEADER_LEN
        );
    }
    let (header, rest) = bytes.split_at(HEADER_LEN);

    if &header[0..8] != &ZHTW_AUTOMATON_MAGIC {
        panic!("zhtw: invalid automaton magic (corrupt binary or wrong format)");
    }

    let header_version = u16::from_le_bytes(header[8..10].try_into().unwrap());
    if header_version != CURRENT_HEADER_VERSION {
        panic!(
            "zhtw: header version mismatch (got {}, expected {})",
            header_version, CURRENT_HEADER_VERSION
        );
    }

    let daachorse_version = u32::from_le_bytes(header[10..14].try_into().unwrap());
    if daachorse_version != DAACHORSE_VERSION_PACKED {
        panic!(
            "zhtw: daachorse version mismatch (built 0x{:08x}, expected 0x{:08x}) — cargo clean && cargo build",
            daachorse_version, DAACHORSE_VERSION_PACKED
        );
    }

    let source_mask = header[22];
    if source_mask != expected.0 {
        panic!(
            "zhtw: automaton source mask mismatch (got {:#04b}, expected {:#04b})",
            source_mask, expected.0
        );
    }

    rest
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn round_trip() {
        let hash = [1, 2, 3, 4, 5, 6, 7, 8];
        let header = build_header(hash, SourceMask::CN_HK);
        let payload = b"hello";
        let mut blob = header.to_vec();
        blob.extend_from_slice(payload);

        let rest = verify_header(&blob, SourceMask::CN_HK);
        assert_eq!(rest, payload);
    }

    #[test]
    #[should_panic(expected = "truncated")]
    fn rejects_short_blob() {
        verify_header(&[0; 10], SourceMask::CN_HK);
    }

    #[test]
    #[should_panic(expected = "magic")]
    fn rejects_bad_magic() {
        let mut blob = [0u8; 28];
        blob[0..8].copy_from_slice(b"XXXXXXXX");
        verify_header(&blob, SourceMask::CN_HK);
    }

    #[test]
    #[should_panic(expected = "source mask")]
    fn rejects_wrong_source_mask() {
        let hash = [0; 8];
        let header = build_header(hash, SourceMask::CN);
        verify_header(&header, SourceMask::CN_HK);
    }
}
