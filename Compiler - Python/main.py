from lexical_analyzer import LexicalAnalyzer

# Example usage of LexicalAnalyzer
if __name__ == "__main__":
    lexical_analyzer = LexicalAnalyzer()

    # Example text for analysis
    # Read the content from input.txt
    with open('input.txt', 'r') as file:
        example_text = file.read()

    # Analyze the example text
    tokens = lexical_analyzer.analyze(example_text)

    # Open a file to write the output
    with open('output.txt', 'w') as output_file:
        # Display the tokens and write to the file
        for token in tokens:
            output_line = f"LINE NUMBER: {str(token.LineNumber).ljust(5)}\tCLASS PART: {str(token.ClassPart).ljust(20)}\tVALUE: {token.Value}\n"
            # print(output_line, end='')  # Print to console
            output_file.write(output_line)  # Write to file

