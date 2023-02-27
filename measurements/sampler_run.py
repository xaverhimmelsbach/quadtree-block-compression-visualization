from run_utils import run_visualization_and_timings, INTERPOLATORS


def sampler_run(input_file):
    input_path = f'./data/input/{input_file}'

    for downsampler in INTERPOLATORS:
        for upsampler in INTERPOLATORS:
            print(f'{downsampler}-{upsampler}')
            run_visualization_and_timings(input_path,
                                          name=f'sampling_{downsampler}_{upsampler}_run',
                                          similarity_cutoff='0.85',
                                          downsampling_interpolator=downsampler,
                                          upsampling_interpolator=upsampler,
                                          archive_format='zip',
                                          encoding_parallelism='False',
                                          skip_oob_blocks='False',
                                          deduplicate_blocks_enable='False',
                                          deduplicate_blocks_minimal_similarity='0.85',
                                          decoding_parallelism='False')
