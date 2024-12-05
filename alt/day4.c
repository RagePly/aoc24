#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define bounds(x, l) (0 <= x && x < l)
int is_xmas(int x, int y, int dx, int dy, char **m, int w, int h) {
    static char *xmas = "XMAS";
    for (int i = 0; i < 4; i++) {
        int xp = x + dx * i;
        int yp = y + dy * i;

        if (!(bounds(xp, w) && bounds(yp, h)) || xmas[i] != m[yp][xp]) {
            return 0;
        }
    }

    return 1;
}

int is_mas(int x, int y, int dx, int dy, char **m, int w, int h) {
    static char *mas = "MAS";
    for (int i = -1; i < 2; i++) {
        int xp = x + dx * i;
        int yp = y + dy * i;

        if (!(bounds(xp, w) && bounds(yp, h)) || mas[i + 1] != m[yp][xp]) {
            return 0;
        }
    }

    return 1;
}

int main(int argc, char **argv) {
    FILE *fp = fopen(argv[1], "r");
    fseek(fp, 0, SEEK_END);
    long len = ftell(fp);    
    fseek(fp, 0, SEEK_SET);
    
    char *fc = malloc(len);
    fread(fc, len, 1, fp);
    fclose(fp);

    char *nl = strstr(fc, "\n"); 
    int width = (int) ((size_t) nl - (size_t) fc);
    
    char **m = malloc(sizeof(char *) * 1024);
    int height = 0;
    for (int i = 0; i < len; i += (width + 1)) {
        m[height ++] = fc + i;
    }
    
    int s1 = 0;
    int s2 = 0;
    for (int x = 0; x < width; x++) {
        for (int y = 0; y < height; y++) {
            int dx[] = {1, 0, 1, 1};
            int dy[] = {0, 1, 1, -1};
            for (int d = 0; d < 4; d++) {
                if (is_xmas(x, y, dx[d], dy[d], m, width, height)) {
                    s1 += 1;
                }
                if (is_xmas(x, y, -dx[d], -dy[d], m, width, height)) {
                    s1 += 1;
                }
            }

            if ((is_mas(x, y, 1, 1, m, width, height) || is_mas(x, y, -1, -1, m, width, height))&& 
                (is_mas(x, y, 1, -1, m, width, height) || is_mas(x, y, -1, 1, m, width, height))) {
                s2 += 1;
            }
        }
    }
    free(m);
    free(fc);

    printf("part1: %d\npart2: %d\n", s1, s2);
    return 0;
}
