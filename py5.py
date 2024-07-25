while True:
    Quote = input ("Enter a quote... If you write Done then loop end but if you wanna continue then start quote with a # ")

    if Quote.lower=='done':
        break
    
    if Quote.startswith=='#':
        continue

    print(Quote)
