import dask.distributed

# Ignore VCF files during pytest collection, so it doesn't fail if cyvcf2 isn't installed.
collect_ignore_glob = ["benchmarks/**", "sgkit/io/vcf/*.py", ".github/scripts/*.py"]

dask.config.set({"distributed.scheduler.allowed-failures": 1})
dask.config.set({"optimization.fuse.active": False})

# Ensure we are testing using dask workers that have to communicate
client = dask.distributed.Client(n_workers=1, threads_per_worker=1)

# Wait for enter to be pressed
input("Press enter to continue")


def pytest_configure(config) -> None:  # type: ignore
    # Add "gpu" marker
    config.addinivalue_line("markers", "gpu:Run tests that run on GPU")
