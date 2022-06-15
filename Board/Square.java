package Chess;
public class Square {
    private Piece contained;

    public Square() {
        contained = Null;
    }

    public Piece getContained() {
        return contained;
    }

    public boolean containsWhite() {
        return getContained().isWhite();
    }

    public void replacePiece(p) {
        contained = p;
    }
}