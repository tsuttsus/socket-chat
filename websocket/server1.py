# ソケット通信(サーバー側)
import socket

host1 = '127.0.0.1'
port1 = 8765

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind((host1, port1))
socket1.listen(1)

print('クライアントからの入力待ち状態')

# コネクションとアドレスを取得
connection, address = socket1.accept()
print('接続したクライアント情報:'  + str(address))

# 無限ループ　byeの入力でループを抜ける
recvline = ''
sendline = ''
num = 0
while True:

    # クライアントからデータを受信
    recvline = connection.recv(4096).decode()

    if recvline == 'bye':
        break

    try:
        num = int(recvline)

        if num % 2 == 0:
            sendline = 'OKです'.encode('utf-8')
        else:
            sendline = 'NGです'.encode('utf-8')
        connection.send(sendline)

    except ValueError as e:
        # 送信用の文字を送信
        sendline = '数値を入力して下さい'.encode('utf-8')
        connection.send(sendline)
    finally:
        print('クライアントで入力された文字＝' + str(recvline))
        
# クローズ
connection.close()
socket1.close()
print('サーバー側終了です')