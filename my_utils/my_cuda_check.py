import torch

if __name__ == '__main__':
    cuda_available = torch.cuda.is_available()
    print("cuda_available: ", cuda_available)
    torch_version = torch.__version__
    # 查看是否是gpu cuda版本的torch，如果显示"2.2.0+cu121"，表示torch版本为2.2.0，支持cuda12.1
    # 电脑安装的cuda版本最好与torch的cuda版本一样，但高于torch的cuda版本一般也可以
    print("torch_version: ", torch_version)