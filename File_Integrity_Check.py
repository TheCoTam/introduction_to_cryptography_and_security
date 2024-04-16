from cryptography.hazmat.primitives import hashes

BLOCK_SIZE = 1024
filePath = 'data_for_File_Integrity_Check/birthday.mp4'
blockList = []


def cal_block_hash(block_data):
    # Tạo một đối tượng hash SHA256
    sha256_hash = hashes.Hash(hashes.SHA256())
    # Cập nhật dữ liệu của khối đang xét vào context hash
    sha256_hash.update(block_data)
    # trả về giá trị băm của khối đang xét
    return sha256_hash.finalize()


# mở file cần xác thực
with open(filePath, "rb") as file:
    while True:
        # Đọc 1KB dữ liệu từ file
        data = file.read(BLOCK_SIZE)
        if not data:
            break
        #  vào danh sách các khối
        blockList.append(data)

# xét từ cuối cùng trong danh sách các khối
for i in range(len(blockList) - 1, -1, -1):
    # sinh mã hash của khối hiện tại
    cur_block_hash = cal_block_hash(blockList[i])
    # nếu là khối đầu tiên thì in ra giá trị hash h0
    if i == 0:
        print(cur_block_hash.hex())
        break

    blockList[i - 1] += cur_block_hash
