// module1/mod.rs

pub fn public_function() {
    println!("called `module1::public_function()`");
}

fn private_function() {
    println!("called `module1::private_function()`");
}

pub mod cmd;
pub mod txt;