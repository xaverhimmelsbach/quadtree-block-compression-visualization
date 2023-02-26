import yaml
import subprocess
import os
import re
import time

INPUT_FILES = [
    "test_black_white.png",
    "test_detail_high.png",
    "test_fine_print.png",
    "test_large.png",
    "test_pixel.png",
    "test_tiny.png",
    "test_color.png",
    "test_detail_low.png",
    "test_gradient.png",
    "test_medium.png",
    "test_small.png"
]

INTERPOLATORS = [
    "NearestNeighbor",
    "ApproxBiLinear",
    "BiLinear",
    "CatmullRom",
]

SIMILARITIES = [
    "0.0",
    "0.1",
    "0.2",
    "0.3",
    "0.4",
    "0.5",
    "0.6",
    "0.7",
    "0.8",
    "0.9",
    "1.0",
]

ARCHIVE_FORMAT = [
    "zip",
    "gzip"
]

CONFIG_YAML_PATH = './configs/config.yml'

CONFIG_YAML = '''
Quadtree:
  SimilarityCutoff: %s
  DownsamplingInterpolator: %s
  UpsamplingInterpolator: %s

Encoding:
  ArchiveFormat: %s
  Parallelism: %s
  SkipOutOfBoundsBlocks:
    Enable: %s
  DeduplicateBlocks:
    Enable: %s
    MinimalSimilarity: %s

Decoding:
  Parallelism: %s

Visualization:
  Enable: %s
'''


def run(input_path, similarity_cutoff, downsampling_interpolator, upsampling_interpolator, archive_format, encoding_parallelism, skip_oob_blocks, deduplicate_blocks_enable, deduplicate_blocks_minimal_similarity, decoding_parallelism, visualization) -> bytes:
    config = CONFIG_YAML % (similarity_cutoff,
                            downsampling_interpolator,
                            upsampling_interpolator,
                            archive_format,
                            encoding_parallelism,
                            skip_oob_blocks,
                            deduplicate_blocks_enable,
                            deduplicate_blocks_minimal_similarity,
                            decoding_parallelism,
                            visualization)

    config_yaml = yaml.safe_load(config)

    with open(CONFIG_YAML_PATH, 'w') as file:
        yaml.dump(config_yaml, file)

    output = './data/output/out'

    result = subprocess.check_output(
        f'./codec -input {input_path} -output {output} -analyticsDir ./data/analytics -config ./configs/config.yml',
        shell=True)

    os.remove(CONFIG_YAML_PATH)

    return result


def plain_run(input_file):
    input_path = f'./data/input/{input_file}'

    similarity_cutoff = '0.9'
    downsampling_interpolator = 'NearestNeighbor'
    upsampling_interpolator = 'NearestNeighbor'
    archive_format = 'zip'
    encoding_parallelism = 'False'
    skip_oob_blocks = 'False'
    deduplicate_blocks_enable = 'False'
    deduplicate_blocks_minimal_similarity = '0.9'
    decoding_parallelism = 'False'

    # Visualization run
    visualization = 'True'
    result = run(input_path, similarity_cutoff, downsampling_interpolator, upsampling_interpolator, archive_format, encoding_parallelism,
        skip_oob_blocks, deduplicate_blocks_enable, deduplicate_blocks_minimal_similarity, decoding_parallelism, visualization)

    analytics = re.search('data\/analytics\/(\d+)', result.decode("utf-8"))

    if analytics is None:
        print('Malformed result')
        return
    
    path = analytics.group(0)
    id = analytics.group(1)

    # Timing run
    visualization = 'False'
    start = time.time()
    run(input_path, similarity_cutoff, downsampling_interpolator, upsampling_interpolator, archive_format, encoding_parallelism,
        skip_oob_blocks, deduplicate_blocks_enable, deduplicate_blocks_minimal_similarity, decoding_parallelism, visualization)
    end = time.time()

    with open(f'{path}/time.txt', 'w') as file:
        file.write(f'{end - start}')


if __name__ == '__main__':

    print("Plain run")

    for input_file in INPUT_FILES:
      print(input_file)
      plain_run(input_file)
