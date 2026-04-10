use criterion::{black_box, criterion_group, criterion_main, Criterion, Throughput};

fn bench_check_single(c: &mut Criterion) {
    let text = "这个软件需要优化";
    c.bench_function("check/single_sentence", |b| {
        b.iter(|| zhtw::check(black_box(text)))
    });
}

fn bench_check_throughput(c: &mut Criterion) {
    let mut group = c.benchmark_group("check/throughput");
    let text = "这个软件需要优化，服务器的用户权限请联系管理员。".repeat(1024 * 1024 / 72);
    group.throughput(Throughput::Bytes(text.len() as u64));
    group.bench_function("1MB", |b| b.iter(|| zhtw::check(black_box(&text))));
    group.finish();
}

criterion_group!(benches, bench_check_single, bench_check_throughput,);
criterion_main!(benches);
