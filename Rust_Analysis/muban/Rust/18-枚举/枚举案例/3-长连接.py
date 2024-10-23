sentence = f'''\
#[derive(Debug)]
enum Websocket {{
    Tcp(Websocket<TcpStream>),
    Tls(Websocket<native_tls::TlsStream<TcpStream>>),
}}

fn new (stream: TcpStream) {{
    let mut s = stream;
    if tls {{
      s = negotiate_tls(stream)
    }}

    // websocket是一个WebSocket<TcpStream>或者
    //   WebSocket<native_tls::TlsStream<TcpStream>>类型
    websocket = WebSocket::from_raw_socket(
      s, ......)
}}
'''
print(sentence)