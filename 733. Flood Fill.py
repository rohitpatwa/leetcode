# Recursively perform DFS. Store startColor, update the pixel and compare it's neighbors with the start color.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not image or not image[0]:
            return image
        
        if image[sr][sc]==newColor:
            return image
        
        startColor = image[sr][sc]
        image[sr][sc] = newColor
        
        if sr-1>=0 and image[sr-1][sc] == startColor:
            self.floodFill(image, sr-1, sc, newColor)
        if sr+1<len(image) and image[sr+1][sc] == startColor:
            self.floodFill(image, sr+1, sc, newColor)
        if sc-1>=0 and image[sr][sc-1] == startColor:
            self.floodFill(image, sr, sc-1, newColor)
        if sc+1<len(image[0]) and image[sr][sc+1] == startColor:
            self.floodFill(image, sr, sc+1, newColor)
        return image 