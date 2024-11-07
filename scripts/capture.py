import cv2
import numpy as np
import mss

class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()
        self.frame = None

    def get_screen(self):
        screenshot = self.sct.grab(self.sct.monitors[1])
        self.frame = np.array(screenshot)
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGBA2BGR)
        return self.frame

    def search_image(self, image_path):
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if template is None:
            return None
        
        frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)
        
        threshold = 0.8
        locations = np.where(result >= threshold)
        
        if len(locations[0]) > 0:
            coordinates = list(zip(locations[1], locations[0]))
            return coordinates
        else:
            return None

    def search_images(self, folder_path):
        if not os.path.isdir(folder_path):
            return None
        
        images_found = []
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            
            if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                coordinates = self.search_image(image_path)
                if coordinates:
                    images_found.append((image_name, coordinates))
        
        if images_found:
            return images_found
        else:
            return None

    def search_onpos(self, image_path, box):
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if template is None:
            return None
        
        frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        x, y, w, h = box
        cropped_frame = frame_gray[y:y+h, x:x+w]
        result = cv2.matchTemplate(cropped_frame, template, cv2.TM_CCOEFF_NORMED)
        
        threshold = 0.8
        locations = np.where(result >= threshold)
        
        if len(locations[0]) > 0:
            coordinates = [(x + loc[0], y + loc[1]) for loc in zip(locations[1], locations[0])]
            return coordinates
        else:
            return None

    def show_screen(self):
        if self.frame is not None and self.frame.size > 0:
            cv2.imshow("Tela Capturada", self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
        else:
            print("Erro: Nenhuma captura de tela foi realizada!")
