"""
--Naim Sen--
Implements upload of file given by command line arg
"""


import argparse
import onedrivesdk
import setup



if __name__ == "__main__":
    # authenticate api
    client = setup.authenticate()

    # create parser for shell arguments
    parser = argparse.ArgumentParser(description='Upload specified file to onedrive')
    parser.add_argument('folderpath', type=str,
                        help='path to upload source')

    args = parser.parse_args()
    source_path = args.folderpath

#    returned_item = client.item(drive='me', id='root').children[source_path].upload(source_path)

    print(client.item(drive='me', id='root').children.shape)
