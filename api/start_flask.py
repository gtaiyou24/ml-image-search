import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.presentation.controller import ImageSearchController


if __name__ == "__main__":
    ImageSearchController.run(debug=True)
