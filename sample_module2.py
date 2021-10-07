from sample_module import bootcamp_name

new_name = bootcamp_name * 2
bootcamp_name = new_name

def double_string(string):
    return string * 2

def main():
    print(double_string(bootcamp_name))

if __name__ == '__main__':
    main()