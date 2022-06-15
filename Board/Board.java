package Chess;
public class Board {
    private Square[][] pieces;

    public Board() {
        pieces = new Square[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                pieces[i][j] = new Square();
            }
        }
    }
}
