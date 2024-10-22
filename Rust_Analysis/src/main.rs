#![allow(unused_variables)]
#![allow(unused_mut)]  // warning: variable does not need to be mutable
#![allow(unused_assignments)]
#![allow(unused_imports)]  // warning: unused import: `std::i8`
#![allow(dead_code)]  // warning: fields `x` and `y` are never read

/*
#![allow(unused_imports)]
#![allow(path_statements)]

#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::fmt::Debug;  // 结构体
use std::path::PathBuf;  // 拼接路径
use std::fs;  // 获取目录
use std::collections::HashMap; // 键值对

// use std::io;
use std::collections::HashSet;  // 去重
// 写数据
use std::fs::OpenOptions;
use std::io::Write;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;




/*
https://www.filepicker.io/api/file/BX9fr87TTu3wtPRRbVLQ
https://github.com/thunlp/THULAC-Python
https://github.com/ibeatai/beat-ai
1 手动分隔
2 同义词替换  新建,建立,创建-->新建
3 满足特征链 就返回
*/

// 定义 所有词性
#[derive(Debug, PartialEq, Clone)]
#[allow(dead_code)]
enum PosTag {
    Pronoun,    // 代词
    Numeral,    // 数词
    Quantifier, // 量词
    NumQuant,   // 数量词
    Verb,       // 动词
    FixedPhrase,// 固定短语
    Conjunction,// 连词
    Preposition,// 介词
    Noun,       // 名词
    PlaceName,  // 地名
    PersonName, // 人名
    Interjection,// 叹词
    Onomatopoeia,// 拟声词
    Adjective,  // 形容词
    Adverb,     // 副词
    TimeWord,   // 时间词
    Directional,// 方位词
    Abbreviation,// 简称
    Particle,   // 助词
    ModalParticle,// 语气助词
    Punctuation,// 标点
    Unknown,    // 未知
}

 */


 fn main() {
    let mut s = String::from("hello");
    s.push_str(", world!"); // push_str() 在字符串后追加字面值
    println!("{}", s); // 将打印 `hello, world!`
 }