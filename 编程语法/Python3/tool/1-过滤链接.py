

def filter_urls(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip().startswith('http'):
                print(line)
                outfile.write(line)

input_file=r"dc\url3.txt"
output_file=r"dc\url_deal3.txt"
filter_urls(input_file, output_file)
