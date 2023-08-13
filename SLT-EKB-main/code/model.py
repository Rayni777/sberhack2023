import numpy as np
import onnxruntime as rt
from einops import rearrange
from sys import platform
import array
from tkinter import *
import tkinter
from tkinter import Tk, Label


def decode_preds(data):
    if platform =='win32' or platform =='win64':
        data = [i.encode('cp1251').decode('utf-8') for i in data]
    return data

class Predictor:
    def __init__(self, model_config, model_type="S3D"):
        """
        Initialize the Predictor class.

        Args:
            model_config (dict): Model configuration containing path_to_model,
                path_to_class_list, threshold, and topk values.
        """
        self.config = model_config
        self.model_type = model_type
        self.model_run(self.config["path_to_model"])

        with open(self.config["path_to_class_list"], "r") as f:
            labels = [line.strip() for line in f]
            labels = decode_preds(labels)

            idx_lbl_pairs = [x.split("\t") for x in labels]
            self.labels = {int(x[0]): x[1] for x in idx_lbl_pairs}

        self.threshold = self.config["threshold"]

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def predict(self, x):
        """
        Make a prediction using the provided input frames.

        Args:
            x (list): List of input frames.

        Returns:
            dict: Dictionary containing predicted labels and confidence values.
        """
        clip = np.array(x).astype(np.float32) / 255.0

        if self.model_type == "S3D":
            clip = rearrange(clip, "t h w c -> 1 c t h w")
        else:
            clip = rearrange(clip, "t h w c -> 1 1 c t h w")

        prediction = self.model([self.output_name], {self.input_name: clip})[0]
        prediction = self.softmax(prediction)
        prediction = np.squeeze(prediction)
        topk_labels = prediction.argsort()[-self.config["topk"] :][::-1]
        topk_confidence = prediction[topk_labels]
        # topk_confidence = topk_confidence * 1000
        result = [self.labels[lbl_idx] for lbl_idx in topk_labels]
        

        
                
        def get_frame(self):
            if self.vid.isOpened():
                ret, frame = self.vid.read()
                if ret:
                    # Return a boolean success flag and the current frame converted to BGR
                    return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    return (ret, None)
            else:
                return (ret, None)
            
        if np.max(topk_confidence) < self.threshold:
            return None
        else:
            print (result)
            #ДОМ КАРТА ЧЕЛОВЕК
            if result == ['карта']:
                print('карта')
            if result == ['человек']:
                print('человек')
            if result == ['дом']:
                print('дом')          
                app = Tk()
                app.title("Gesturelearn")
                app.geometry("400x600") # размер окна
                text = "Верно!"
                background = "#FFFFFF" # белый цвет
                app.configure(bg=background)
                #image7 = PhotoImage(file="true.png")
                #label10 = Label(app, image=image7)
                #label10.config(width=300, height=300)
                #label10.place(relx=0.5, rely=0.3, anchor=CENTER) # размещаем по центру
                label9 = Label(app, text=text, font=("Arial", 20), bg=background)
                label9.pack()
                #image7 = PhotoImage(file="true.png")
                #label7 = Label(app, image=image7)
                #label7.place(relx=0.5, rely=0.7, anchor=CENTER) # размещаем по центру                
                app.mainloop()
            if result == ['день']:
                print('день')
                app = Tk()
                app.title("Gesturelearn")
                app.geometry("400x600") # размер окна
                text = "Верно!"
                background = "#FFFFFF" # белый цвет
                app.configure(bg=background)
                #image7 = PhotoImage(file="true.png")
                #label10 = Label(app, image=image7)
                #label10.config(width=300, height=300)
                #label10.place(relx=0.5, rely=0.3, anchor=CENTER) # размещаем по центру
                label9 = Label(app, text=text, font=("Arial", 20), bg=background)
                label9.pack()
                #image7 = PhotoImage(file="true.png")
                #label7 = Label(app, image=image7)
                #label7.place(relx=0.5, rely=0.7, anchor=CENTER) # размещаем по центру                
                app.mainloop()

                
                
            return {
                "labels": dict(zip([i for i in range(len(result))], result)),
                "confidence": dict(
                    zip([i for i in range(len(result))], topk_confidence)
                ),
            
            }
            


        

    def model_run(self, path_to_model: str) -> None:
        """
        Load and run the ONNX model using the provided path.

        Args:
            path_to_model (str): Path to the ONNX model file.

        Returns:
            None
        """
        session = rt.InferenceSession(
            path_to_model, providers=["CPUExecutionProvider"]
        )
        self.input_name = session.get_inputs()[0].name
        self.output_name = session.get_outputs()[0].name

        self.model = session.run

    def decode_preds(self, data):
        if platform =='win32' or platform =='win64':
            data = [i.encode('cp1251').decode('utf-8') for i in data]
        return data

