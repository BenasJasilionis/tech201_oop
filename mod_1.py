# Variable __name__ gets set to __main__ by default

  # In this case name == main # Output = __main__

def main():
    #pass      # Means Null/ None
    print("This is mod1's name ->" + __name__)
if __name__ == "__main__":
    main()

# Checking if what is being ran is being ran in the current file or somewhere else