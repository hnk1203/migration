import zipfile
import tarfile

# def extract_zip(zip_file_path, extract_to_path):
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to_path)

def extract_tar(tar_file_path, extract_to_path2):
    with tarfile.open(tar_file_path, 'r') as tar_ref:
        tar_ref.extractall(extract_to_path2)

def extract_tar(tar_file_path2, extract_to_path3):
    with tarfile.open(tar_file_path2, 'r') as tar_ref:
        tar_ref.extractall(extract_to_path3)

if __name__ == "__main__":
    # # zip 파일 압축 해제
    # zip_file_path = './building-train_images_targets.zip'
    # extract_to_path = './image_sampled'
    # extract_zip(zip_file_path, extract_to_path)

    # tar 파일 압축 해제1
    tar_file_path1 = './train_images_labels_targets.tar'
    extract_to_path2 = './image_origin'
    extract_tar(tar_file_path1, extract_to_path2)
    
    # tar 파일 압축 해제2
    tar_file_path2 = './test_images_labels_targets.tar'
    extract_to_path3 = './image_test'
    extract_tar(tar_file_path2, extract_to_path3)