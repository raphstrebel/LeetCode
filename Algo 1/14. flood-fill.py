class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        nrows = len(image)
        ncols = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def fillRec(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r > 0:
                    # fill upper cell
                    fillRec(r-1, c)
                if r < nrows-1:
                    # fill lower cell
                    fillRec(r+1, c)
                if c > 0:
                    # fill left cell
                    fillRec(r, c-1)
                if c < ncols-1:
                    # fill left cell
                    fillRec(r, c+1)
        fillRec(sr, sc)
        return image