sentence = f'''\
#[derive(Debug)]
enum PokerCard {{
    Clubs(u8),
    Spades(u8),
    Diamonds(u8),
    Hearts(u8),
}}

fn print_suit(card: PokerCard) {{
    // 需要在定义 enum PokerSuit 的上面添加上 #[derive(Debug)]，否则会报 card 没有实现 Debug
    println!("{{:?}}",card);
}}

fn main() {{
    let heart: PokerCard = PokerCard::Hearts(10);
    let diamond: PokerCard = PokerCard::Diamonds(20);
    print_suit(heart);
    print_suit(diamond);
}}

/*
Hearts(10)
Diamonds(20)
*/
'''
print(sentence)