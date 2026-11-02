#A2_huffman

import heapq

# Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


# Huffman Encoding
def huffman_encoding(chars, freq):
    heap = []

    # Insert nodes into Min Heap
    for i in range(len(chars)):
        node = Node(chars[i], freq[i])
        heapq.heappush(heap, (freq[i], i, node))

    count = len(chars)

    # Build Huffman Tree
    while len(heap) > 1:

        # Extract two minimum frequency nodes
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        # Create new internal node
        new_node = Node(None, f1 + f2)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, (new_node.freq, count, new_node))
        count += 1

    root = heap[0][2]

    # Generate Huffman Codes
    codes = {}

    def generate_codes(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code if code else "0"
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")

    return codes


# Main Program
def main():

    n = int(input("Enter number of characters: "))

    chars = []
    freq = []

    # Take input from user
    for i in range(n):
        ch = input("Enter character: ")
        f = int(input("Enter frequency: "))

        chars.append(ch)
        freq.append(f)

    # Call Huffman function
    codes = huffman_encoding(chars, freq)

    # Display Huffman Codes
    print("\nHuffman Codes")
    print("----------------------")

    total_bits = 0

    for i in range(n):
        print(chars[i], ":", codes[chars[i]])
        total_bits += freq[i] * len(codes[chars[i]])

    print("----------------------")
    print("Total encoded bits:", total_bits)


if __name__ == "__main__":
    main()