sentence = f'''\
#[derive(Debug)]
enum PokerSuit {{
    Clubs,
    Spades,
    Diamonds,
    Hearts,
}}

fn print_suit(card: PokerSuit) {{
    // 需要在定义 enum PokerSuit 的上面添加上 #[derive(Debug)]，否则会报 card 没有实现 Debug
    println!("{{:?}}",card);
}}

fn main() {{
    let heart: PokerSuit = PokerSuit::Hearts;
    let diamond: PokerSuit = PokerSuit::Diamonds;
    print_suit(heart);
    print_suit(diamond);
}}
'''
print(sentence)