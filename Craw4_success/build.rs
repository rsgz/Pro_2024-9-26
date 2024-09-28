extern crate embed_resource;

fn main(){
    embed_resource::compile(r"./icon.rc",embed_resource::NONE);
}

// use std::env;

// fn main() {
//     let is_release = env::var("PROFILE").unwrap() == "release";
//     if is_release {
//         // let manifest_dir = env::var("CARGO_MANIFEST_DIR").unwrap();
//         let mut res = winres::WindowsResource::new();
//         res.set_icon(r"D:\58-anaconda\install2\pkgs\spyder-5.5.1-py312haa95532_0\Scripts\spyder.ico"); // 替换为你的图标路径
//         res.compile().unwrap();
//     }
// }
