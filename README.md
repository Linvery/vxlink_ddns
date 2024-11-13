# 项目名称

## 简介
该项目使用 Python 实现了一个与 vx.link API 交互的工具，能够获取和编辑 vxtrans 的 IPv6 地址。

## 文件说明

- `vxlink.py`：包含与 vx.link API 交互的类 `VxLink`，实现了登录、获取 vxtrans 列表和编辑 vxtrans IPv6 地址的功能。
- `tools.py`：包含获取公共 IPv6 地址的工具函数。
- `main.py`：主程序文件，演示了如何使用 `tools.py` 和 `vxlink.py` 中的功能。

## 安装

1. 克隆仓库到本地：
    ```bash
    git clone <仓库地址>
    cd <仓库目录>
    ```

2. 创建并激活虚拟环境：
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate  # Windows
    ```

3. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. 编辑 `main.py` 文件，设置你的 vx.link 用户名和密码：
    ```python
    username = "your_username"
    password = "your_password"
    ```

2. 运行主程序：
    ```bash
    python main.py
    ```

## 功能说明

### 获取公共 IPv6 地址

`tools.py` 文件中的 `get_public_ipv6_addresses` 函数会返回一个包含所有公共 IPv6 地址的字典。

### 登录 vx.link

`vxlink.py` 文件中的 `VxLink` 类实现了登录 vx.link 的功能。初始化 `VxLink` 对象时会自动进行登录。

### 获取vxtrans 列表

`VxLink` 类中的 `get_vxtrans_list` 方法会返回当前用户的 vxtrans 列表。

### 编辑 vxtrans 的 IPv6 地址

`VxLink` 类中的 `edit_vxtrans_ipv6` 方法可以编辑指定 vxtrans 的 IPv6 地址。

## 许可证

该项目使用 MIT 许可证，详情请参见 LICENSE 文件。