sentence = f'''\
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ .email 方式修改 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    // 定义结构体
    struct User {{
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }}

    // 创建 结构体 实例
    let mut user1 = User {{
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    }};
    // 修改结构体
    user1.email = String::from("anotheremail@example.com");
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ user1 实例来构建 user2 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
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

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ user1 部分属性构建 user2 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
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
    
    // user1 部分属性 赋值给user2
    let user2 = User {{
        email: String::from("another@example.com"),  // 只写修改的部分
        ..user1
    }};
    println!("{{:?}}",user2);

}}
'''
print(sentence)