head = input()
article = input()
print("<h1>")
print(f"    {head}")
print("</h1>")
print("<article>")
print(f"    {article}")
print("</article>")
while True:
    content = input()
    if content == "end of comments":
        break
    print("<div>")
    print(f"    {content}")
    print("</div>")
