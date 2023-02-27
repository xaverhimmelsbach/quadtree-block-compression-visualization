from run_utils import run_visualization_and_timings, ARCHIVE_FORMAT


def compression_run(input_file):
    input_path = f'./data/input/{input_file}'

    for archive_format in ARCHIVE_FORMAT:
        print(archive_format)
        run_visualization_and_timings(input_path,
                                      name=f'compression_{archive_format}_run',
                                      similarity_cutoff='0.85',
                                      downsampling_interpolator='ApproxBiLinear',
                                      upsampling_interpolator='ApproxBiLinear',
                                      archive_format=archive_format,
                                      encoding_parallelism='False',
                                      skip_oob_blocks='False',
                                      deduplicate_blocks_enable='False',
                                      deduplicate_blocks_minimal_similarity='0.85',
                                      decoding_parallelism='False')
