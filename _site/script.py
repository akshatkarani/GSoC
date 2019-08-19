import os

import requests

patches = {
    'cEP': {'001': ['https://github.com/coala/cEPs/pull/182.patch',
                    'coala-enhancement-proposal-for-next-gen-action-system-project.patch']
            },
    'coala': {'001': ['https://github.com/coala/coala/pull/6039.patch',
                      'Modifying-color_letter-function.patch'],
              '002': ['https://github.com/coala/coala/pull/6029.patch',
                      'Adding-actions-attribute.patch'],
              '003': ['https://github.com/coala/coala/pull/6046/commits/12d887e684dd57fc399c2687834838119fdd5e52.patch',
                      'Tutorial-for-writing-bear-actions.patch'],
              '004': ['https://github.com/coala/coala/pull/6057/commits/bba1cb7a16a958891edfa4a9f422e03767d9ec0f.patch',
                      'Support-for-multiple-patches.patch'],
              '005': ['https://github.com/coala/coala/pull/6060.patch',
                      'Update-docs-to-explain-multiple-patches.patch']
              },
    'coala-bears': {

        '001': ['https://github.com/coala/coala-bears/pull/2927/commits/bab86b2383d9e2541c1a626ecea763c7a0b44be8.patch',
                'EditCommitMessageAction-for-GitCommitBear.patch'],
        '002': ['https://github.com/coala/coala-bears/pull/2927/commits/1ebb34f4b8f3f030997fe0c619c798bcece2bfba.patch',
                'AddNewlineAction-for-GitCommitBear.patch'],
        '003': ['https://github.com/coala/coala-bears/pull/2947/commits/993e86c80ee5fd290329bbe53ab11fa02e06eeb5.patch',
                'Remove-file-argument-DuplicateFileBear.patch'],
        '004': ['https://github.com/coala/coala-bears/pull/2947/commits/74c83e0a20ad6ac18257929aebc6cdd9471e140b.patch',
                'DeleteFileAction-for-DuplicateFileBear.patch'],
        '005': ['https://github.com/coala/coala-bears/pull/2948/commits/1410d617120cb2943f72dc162b579665dd45b9cf.patch',
                'Provide-multiple-patches-FilenameBear.patch']
    }

}

main_folder = 'gsoc_patches'


def download_cached_file(url, filename):
    response = requests.get(url, stream=True, timeout=20)
    response.raise_for_status()

    with open(filename, 'ab') as file:
        for chunk in response.iter_content(125):
            file.write(chunk)


if __name__ == '__main__':
    import time
    import logging

    main_dir = os.path.join(os.path.abspath(os.getcwd()), main_folder)
    os.mkdir(main_dir)
    d = {}
    for name, d in patches.items():
        dir_name = os.path.join(main_dir, name)
        os.mkdir(dir_name)
        for num, lst in d.items():
            download_cached_file(lst[0], os.path.join(dir_name, num + '-' + lst[1]))
            logging.info('Downloaded {} as {}'.format(lst[0], lst[1]))
            time.sleep(3)

