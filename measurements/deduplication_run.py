from run_utils import run_visualization_and_timings, SIMILARITIES


def deduplication_run(input_file):
    input_path = f'./data/input/{input_file}'

    for similarity in SIMILARITIES:
        print(similarity)
        run_visualization_and_timings(input_path,
                                      name=f'deduplication_{similarity}_run',
                                      similarity_cutoff='0.85',
                                      downsampling_interpolator='ApproxBiLinear',
                                      upsampling_interpolator='ApproxBiLinear',
                                      archive_format='zip',
                                      encoding_parallelism='False',
                                      skip_oob_blocks='False',
                                      deduplicate_blocks_enable='True',
                                      deduplicate_blocks_minimal_similarity=similarity,
                                      decoding_parallelism='False')
