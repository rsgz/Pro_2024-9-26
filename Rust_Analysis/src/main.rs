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
    let text = "Rust 开发团队的意见又非常重视社区的意见";
    let zi = "的意见";

    // 使用 find 方法查找 pattern 在 text 中的位置 非常反直觉 那么使用chars()好一点 
    let fu_list: Vec<char> = text.chars().collect();
    print!("{:?}",fu_list);
    let zi_list: Vec<char> = zi.chars().collect();
    print!("{:?}",zi_list);

    // 首次寻找  假设如果这个字符 只存在一次 那肯定是最左边
    let mut weizhi_l: Vec<usize> = Vec::new();
    let mut shou: bool=false;
    for (i,v1) in fu_list.into_iter().enumerate(){
        for (j,v2) in zi_list.clone().into_iter().enumerate(){
            if v1==v2{
                // 第一次 直接录入 索引
                if weizhi_l.len()<1{
                    weizhi_l.push(i);
                }
                // 第2-n次 直接录入 索引   
                // 索引之间 间隔1 保证了 连续性 i-weizhi_l[weizhi_l.len()-1]==1
                // 这个逻辑 获取了最左边的一次
                if weizhi_l.len()>=1 && i-weizhi_l[weizhi_l.len()-1]==1{
                    weizhi_l.push(i);
                }
                // println!(">>>>>> v2 ---> \n{:#?}",i);
            }
        }
    }
    // 
    print!("{:?}",weizhi_l);
}