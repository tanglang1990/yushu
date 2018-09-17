from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)
    # 实际生产环境中不会直接使用flask内置的web服务器
    # 默认是单进程
    # threaded 多线程
    # processes 多进程
