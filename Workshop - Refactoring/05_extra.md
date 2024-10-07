# Extra practice
Use your learned refactoring skills and tooling to clean up the code below.

## Exercises

1. Refactor the `process_data()` function into smaller functions:

    ```python
    def process_data(data):
        # Step 1: Clean data
        cleaned_data = []
        for item in data:
            if item is not None and item != "":
                cleaned_data.append(item.strip())

        # Step 2: Normalize data
        normalized_data = []
        max_value = max(cleaned_data)
        min_value = min(cleaned_data)
        for item in cleaned_data:
            normalized_item = (item - min_value) / (max_value - min_value)
            normalized_data.append(normalized_item)

        # Step 3: Compute statistics
        total = sum(normalized_data)
        count = len(normalized_data)
        mean = total / count if count != 0 else 0
        sorted_data = sorted(normalized_data)
        if count % 2 == 0:
            median = (sorted_data[count // 2 - 1] + sorted_data[count // 2]) / 2
        else:
            median = sorted_data[count // 2]
        variance = sum((x - mean) ** 2 for x in normalized_data) / count
        stddev = variance ** 0.5

        # Step 4: Format results
        result = {
            "mean": mean,
            "median": median,
            "variance": variance,
            "stddev": stddev,
            "count": count
        }
        return result

    # Example usage
    data = [2, 8, 5, None, 10, '', 7]
    print(process_data(data))
    ```
    <details markdown="1">
    <summary align="right">
    Solution: use VSCode's extract method
    </summary>
    <br>

    ```python
    def clean_data(data: str) -> str:
        cleaned_data = []
        for item in data:
            if item is not None and item != "":
                cleaned_data.append(item.strip())

        return cleaned_data

    def normalize_data(data: str) -> str:
        normalized_data = []
        max_value = max(data)
        min_value = min(data)
        for item in data:
            normalized_item = (item - min_value) / (max_value - min_value)
            normalized_data.append(normalized_item)

        return normalized_data

    def compute_statistics(data: str) -> tuple[float, float, float, float, int]:
        total = sum(data)
        count = len(data)
        mean = total / count if count != 0 else 0
        sorted_data = sorted(data)
        if count % 2 == 0:
            median = (sorted_data[count // 2 - 1] + sorted_data[count // 2]) / 2
        else:
            median = sorted_data[count // 2]
        variance = sum((x - mean) ** 2 for x in data) / count
        stddev = variance ** 0.5

        return mean, median, variance, stddev, count

    def format_results(mean: float, median: float, variance: float, stddev: float, count: int) -> dict:
        return {
            "mean": mean,
            "median": median,
            "variance": variance,
            "stddev": stddev,
            "count": count
        }

    def process_data(data: str) -> dict:
        cleaned_data = clean_data(data)
        normalized_data = normalize_data(cleaned_data)
        mean, median, variance, stddev, count = compute_statistics(normalized_data)

        return format_results(mean, median, variance, stddev, count)


    if "__main__" in __name__:
        # Example usage
        data = [2, 8, 5, None, 10, '', 7]
        print(process_data(data))
    ```

    </details>

    <br><br>

2. Apply Object Oriented Programming (OOP) to refactor the following code:

    ```python
    import math

    def compute_area(shape, dimensions):
        if shape == "circle":
            if len(dimensions) != 1:
                return "Error: Circle requires 1 dimension (radius)"
            radius = dimensions[0]
            return math.pi * radius * radius
        elif shape == "rectangle":
            if len(dimensions) != 2:
                return "Error: Rectangle requires 2 dimensions (length and width)"
            length = dimensions[0]
            width = dimensions[1]
            return length * width
        elif shape == "triangle":
            if len(dimensions) != 2:
                return "Error: Triangle requires 2 dimensions (base and height)"
            base = dimensions[0]
            height = dimensions[1]
            return 0.5 * base * height
        else:
            return "Error: Unknown shape"

    # Example usage
    print(compute_area("circle", [5]))
    print(compute_area("rectangle", [4, 5]))
    print(compute_area("triangle", [3, 6]))
    print(compute_area("hexagon", [2, 3]))
    print(compute_area("circle", [5, 2]))
    print(compute_area("rectangle", [4]))
    print(compute_area("triangle", [3]))
    ```
    <details markdown="1">
    <summary align="right">
    Solution: restructure with classes
    </summary>
    <br>

    ```python
    import math

    class Shape:
        def area(self) -> None:
            raise NotImplementedError("This method should be overridden by subclasses")

    class Circle(Shape):
        def __init__(self, radius: float|int) -> None:
            self.radius: float|int = radius

        def area(self) -> float:
            return math.pi * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, length: float|int, width: float|int) -> None:
            self.length: float|int = length
            self.width: float|int = width

        def area(self) -> float:
            return self.length * self.width

    class Triangle(Shape):
        def __init__(self, base: float|int, height: float|int) -> None:
            self.base: float|int = base
            self.height: float|int = height

        def area(self) -> float:
            return 0.5 * self.base * self.height

    def compute_area(shape: Shape) -> float:
        return shape.area()

    # Example usage
    print(compute_area(Circle(5)))
    print(compute_area(Rectangle(4, 5)))
    print(compute_area(Triangle(3, 6)))
    ```

    </details>
    <br><br>

3. Use the idea of an interface to capture the essense of this code:

    ```python
    def process_text_document(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        word_count = len(content.split())
        line_count = len(content.split('\n'))
        return f"Text Document - Words: {word_count}, Lines: {line_count}"

    def process_pdf_document(file_path):
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text()
        word_count = len(content.split())
        page_count = len(reader.pages)
        return f"PDF Document - Words: {word_count}, Pages: {page_count}"

    def process_word_document(file_path):
        import docx
        doc = docx.Document(file_path)
        content = ""
        for paragraph in doc.paragraphs:
            content += paragraph.text + "\n"
        word_count = len(content.split())
        paragraph_count = len(doc.paragraphs)
        return f"Word Document - Words: {word_count}, Paragraphs: {paragraph_count}"

    # Example usage
    print(process_text_document('sample.txt'))
    print(process_pdf_document('sample.pdf'))
    print(process_word_document('sample.docx'))
    ```

    <details markdown="1">
    <summary align="right">
    Solution: with OOP and an interface
    </summary>
    <br>

    ```python
    from abc import ABC, abstractmethod
    from PyPDF2 import PdfReader
    import docx

    class DocumentProcessor(ABC):
        def __init__(self, file_path: str) -> None:
            self.file_path: str = file_path

        @abstractmethod
        def process(self) -> str:
            pass

    class TextDocumentProcessor(DocumentProcessor):
        def process(self) -> str:
            with open(self.file_path, 'r') as file:
                content = file.read()
            word_count = len(content.split())
            line_count = len(content.split('\n'))

            return f"Text Document - Words: {word_count}, Lines: {line_count}"

    class PDFDocumentProcessor(DocumentProcessor):
        def process(self) -> str:
            reader = PdfReader(self.file_path)
            content = ""
            for page in reader.pages:
                content += page.extract_text()
            word_count = len(content.split())
            page_count = len(reader.pages)

            return f"PDF Document - Words: {word_count}, Pages: {page_count}"

    class WordDocumentProcessor(DocumentProcessor):
        def process(self) -> str:
            doc = docx.Document(self.file_path)
            content = ""
            for paragraph in doc.paragraphs:
                content += paragraph.text + "\n"
            word_count = len(content.split())
            paragraph_count = len(doc.paragraphs)

            return f"Word Document - Words: {word_count}, Paragraphs: {paragraph_count}"

    def print_document_info(processor: DocumentProcessor) -> None:
        try:
            print(processor.process())
        except Exception as e:
            print(f"Error processing document: {e}")

    # Example usage
    processor1 = TextDocumentProcessor('sample.txt')
    processor2 = PDFDocumentProcessor('sample.pdf')
    processor3 = WordDocumentProcessor('sample.docx')

    print_document_info(processor1)
    print_document_info(processor2)
    print_document_info(processor3)
    ```

    </details>
    <br><br>

## Need even more practice?
Fire up ChatGPT and ask it to generate examples for you. Use your knowledge of Clean Code and Dirty Code to ask for examples.

**Prompt**

> I need some hands-on examples for a workshop on refactoring with Python.

**Iterate**

> Can you generate an example with a far too long function that needs to be refactored into small functions? Also provide a cleaned up version.