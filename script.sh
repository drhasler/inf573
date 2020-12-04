# adds shape predictor to data folder
[ ! -d data ] && mkdir data
cd data
curl http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 \
    --output shape_predictor_68_face_landmarks.dat.bz2
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
