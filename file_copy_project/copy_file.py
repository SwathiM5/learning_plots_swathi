# DO NOT MODIFY THIS PART
# Create a source file to copy from
with open('source.txt', 'w') as f:
    f.write("This is the content of the source file.")

# Write your function below
def copy_file_content():
    # Your code here
      try:
        with open('source.txt', 'r') as source_file:
          content = source_file.read()

      except FileNotFoundError:
        print("Error: The file 'source.txt' was not found.")

        content = "This is the content of the source file"

      try:    
        with open('destination.txt', 'w') as destination_file:
          destination_file.write(content)
    

      except Exception as e:
        print(f"An unexcepted error occurred: {e}")
  
# Testing mechanism - DO NOT MODIFY!
copy_file_content()
with open('destination.txt', 'r') as f:
   print(f.read())


