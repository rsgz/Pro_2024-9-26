sentence = f'''\
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 方式1 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    // 定义结构体
    struct User {{
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }}

    // 创建 结构体 实例
    let user1 = User {{
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    }};    
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 函数创建结构体 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    // 定义结构体
    #[derive(Debug)]
    struct User {{
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }}

    // 创建 结构体 实例
    fn build_user(email: String, username: String) -> User {{
        User {{
            email: email,
            username: username,
            active: true,
            sign_in_count: 1,
        }}
    }}
    
    let user1 = build_user("2966@xx".to_string(), "rsgz".to_string());
    println!("{{:?}}",user1); // User {{ active: true, username: "rsgz", email: "2966@xx", sign_in_count: 1 }}
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 函数创建结构体2 缩略初始化 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    // 定义结构体
    #[derive(Debug)]
    struct User {{
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }}

    // 创建 结构体 实例
    fn build_user(email: String, username: String) -> User {{
        User {{
            email, // 当函数参数和结构体字段同名时，可以直接使用缩略的方式进行初始化
            username,
            active: true,
            sign_in_count: 1,
        }}
    }}
    
    let user1 = build_user("2966@xx".to_string(), "rsgz".to_string());
    println!("{{:?}}",user1); // User {{ active: true, username: "rsgz", email: "2966@xx", sign_in_count: 1 }}
}}
'''
print(sentence)