import socket

# サーバーのIPアドレスとポート番号
HOST = 'localhost'  # サーバーのIPアドレス
PORT = 12345  # ポート番号

# サーバーに接続するソケットの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーに接続する
    s.connect((HOST, PORT))
    
    # データを送信する
    message = "Hello, server!"
    s.sendall(message.encode())
    
    # サーバーからのレスポンスを受信する
    data = s.recv(1024)
    
    print("サーバーからのレスポンス:", data.decode())