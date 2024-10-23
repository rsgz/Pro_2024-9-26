sentence = f'''\
r"Escapes don't work here: \\x3F \\u{{211D}}";
r#"And then I said: "There is no escape!""#;
r###"A string with "# in it. And even "##!"###;
'''
print(sentence)