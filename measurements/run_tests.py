import run_utils
from plain_run import plain_run
from skip_oob_run import skip_oob_run
from sampler_run import sampler_run
from similarity_run import similarity_run
from compression_run import compression_run
from deduplication_run import deduplication_run
from parallel_run import parallel_run

if __name__ == '__main__':

    print("Plain run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        plain_run(input_file)

    print("Skip OOB run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        skip_oob_run(input_file)

    print("Sampler run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        sampler_run(input_file)

    print("Similarity run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        similarity_run(input_file)

    print("Compression run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        compression_run(input_file)

    print("Deduplication run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        deduplication_run(input_file)

    print("Parallel run")
    for input_file in run_utils.INPUT_FILES:
        print(input_file)
        parallel_run(input_file)
