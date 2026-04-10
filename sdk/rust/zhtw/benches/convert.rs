use criterion::{black_box, criterion_group, criterion_main, BenchmarkId, Criterion, Throughput};

fn bench_convert_single(c: &mut Criterion) {
    let text = "这个软件需要优化";
    c.bench_function("convert/single_sentence", |b| {
        b.iter(|| zhtw::convert(black_box(text)))
    });
}

fn bench_convert_throughput(c: &mut Criterion) {
    let mut group = c.benchmark_group("convert/throughput");
    for size_kb in &[1, 10, 100, 1024] {
        let text = "这个软件需要优化，服务器的用户权限请联系管理员。".repeat(size_kb * 1024 / 72);
        group.throughput(Throughput::Bytes(text.len() as u64));
        group.bench_with_input(
            BenchmarkId::from_parameter(format!("{}KB", size_kb)),
            &text,
            |b, t| b.iter(|| zhtw::convert(black_box(t))),
        );
    }
    group.finish();
}

fn bench_default_instance_access(c: &mut Criterion) {
    let _ = zhtw::convert("warmup");
    c.bench_function("init/default_instance_access", |b| {
        b.iter(|| zhtw::Converter::default_instance())
    });
}

criterion_group!(
    benches,
    bench_convert_single,
    bench_convert_throughput,
    bench_default_instance_access,
);
criterion_main!(benches);
