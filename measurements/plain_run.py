from run_utils import run_visualization_and_timings


def plain_run(input_file):
    input_path = f'./data/input/{input_file}'

    run_visualization_and_timings(input_path,
                                  name='plain_run',
                                  similarity_cutoff='0.85',
                                  downsampling_interpolator='ApproxBiLinear',
                                  upsampling_interpolator='ApproxBiLinear',
                                  archive_format='zip',
                                  encoding_parallelism='False',
                                  skip_oob_blocks='False',
                                  deduplicate_blocks_enable='False',
                                  deduplicate_blocks_minimal_similarity='0.85',
                                  decoding_parallelism='False')