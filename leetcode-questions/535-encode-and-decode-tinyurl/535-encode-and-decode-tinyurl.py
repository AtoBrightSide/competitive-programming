class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.key = random.randint(10,99)
        coded = longUrl.split('/')
        encoded = ""
        for i in range(len(coded)):
            encoded += str(self.key) + coded[i] + "/"
        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decoded = ""
        shortUrl = shortUrl.split('/')
        for i in range(len(shortUrl)):
            if len(shortUrl[i])>2:
                decoded += shortUrl[i][2:] + "/"
            else:
                decoded += "/"
        
        return decoded[:-2]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))