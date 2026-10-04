# Practical 2: Huffman Code

class HuffmanNode:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None


huffman_codes = {}


def get_min(nodes):
    min_index = 0
    for i in range(1, len(nodes)):
        if nodes[i].freq < nodes[min_index].freq:
            min_index = i
    return nodes.pop(min_index)


def generate_codes(node, code):
    if node is None:
        return
    if node.left is None and node.right is None:
        # A single-character text gets code "0" instead of an empty code
        huffman_codes[node.ch] = code if code != "" else "0"
    generate_codes(node.left, code + "0")
    generate_codes(node.right, code + "1")


# Input
text = input("Enter the text: ")

if text == "":
    print("Text is empty, nothing to encode.")
    raise SystemExit

# Frequency calculation
freq_map = {}
for ch in text:
    if ch in freq_map:
        freq_map[ch] += 1
    else:
        freq_map[ch] = 1

# Create nodes
nodes = []
for ch in freq_map:
    nodes.append(HuffmanNode(ch, freq_map[ch]))

# Build Huffman Tree
while len(nodes) > 1:
    left = get_min(nodes)
    right = get_min(nodes)
    parent = HuffmanNode('-', left.freq + right.freq)
    parent.left = left
    parent.right = right
    nodes.append(parent)

root = nodes[0]

# Generate Huffman Codes
generate_codes(root, "")

# Display Codes
print("\nCharacter\tFrequency\tCode")
for ch in huffman_codes:
    label = "(space)" if ch == " " else ch
    print(label, "\t\t", freq_map[ch], "\t\t", huffman_codes[ch])

# Encode Text
encoded = ""
for ch in text:
    encoded += huffman_codes[ch]

print("\nEncoded Text:", encoded)
