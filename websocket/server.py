import socket

# サーバーのIPアドレスとポート番号
HOST = 'localhost'  # サーバーのIPアドレス
PORT = 12345  # ポート番号

# ソケットの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # ソケットを指定したIPアドレスとポート番号にバインドする
    s.bind((HOST, PORT))
    
    # クライアントからの接続を待機する
    s.listen()
    
    print("クライアントからの接続を待機中...")
    
    # クライアントからの接続を受け入れる
    conn, addr = s.accept()
    
    with conn:
        print("クライアントが接続しました。アドレス:", addr)
        
        while True:
            # クライアントからのデータを受信する
            data = conn.recv(1024)
            
            if not data:
                # データが空の場合、クライアントとの接続を終了する
                break
            
            # 受信したデータを処理する（例：エコーバック）
            conn.sendall(data)
