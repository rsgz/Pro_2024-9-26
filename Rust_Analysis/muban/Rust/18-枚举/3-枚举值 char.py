sentence = f'''\
#[derive(Debug)]
enum PokerCard {{
    Clubs(u8),
    Spades(u8),
    Diamonds(char),
    Hearts(char),  // 这是char类型枚举值 
}}


fn print_suit(card: PokerCard) {{
    // 需要在定义 enum PokerSuit 的上面添加上 #[derive(Debug)]，否则会报 card 没有实现 Debug
    println!("{{:?}}",card);
}}

fn main() {{
    let heart: PokerCard = PokerCard::Spades(10);
    let diamond: PokerCard = PokerCard::Diamonds('A');
    print_suit(heart);
    print_suit(diamond);
}}

/*
Spades(10)
Diamonds('A')
*/
'''
print(sentence)