
def lorem_ipsum():
    a = 2
    if a > 3:
        print('a is more than 3')
    lorem_ipsum_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n" 
    lorem_ipsum_text += "Duis ac dui tortor. Nullam dapibus metus ut nibh egestas, a ultricies tellus placerat.\n"
    lorem_ipsum_text += "Fusce vestibulum libero nec justo condimentum dignissim. Vivamus euismod turpis quis leo efficitur blandit.\n"
    lorem_ipsum_text += "Aliquam erat volutpat. Sed id nisl eu nisi lobortis elementum in vel mi. Maecenas eu felis non velit dictum pretium.\n"
    lorem_ipsum_text += "Integer vestibulum, justo sit amet fringilla pharetra, orci nulla malesuada lectus, vitae finibus metus odio ac libero.\n"
    lorem_ipsum_text += "Sed ac turpis ut ante bibendum imperdiet. In hac habitasse platea dictumst. Sed at dolor id sapien gravida condimentum non vel eros.\n"
    lorem_ipsum_text += "Nulla facilisi. Vivamus posuere lacinia ipsum in rutrum. Maecenas auctor, nunc et vestibulum pulvinar, purus turpis varius nulla, eu tincidunt libero leo nec justo."
    
    # Split the text into lines and return the first 10
    return lorem_ipsum_text.split('\n')

def another_function(
    n1: int,
    n2: int
):
    return n2 > n1