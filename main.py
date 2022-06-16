from os import listdir, mkdir, path
from shutil import move


class FileOrganizer:
    """Organize files of given location or downloads directory."""

    LOCATION = "C://Users//Sahil//Downloads"

    IMAGE_EXT = [".jpg", ".png", ".jpeg", ".gif", ".webp", ".eps"]
    DOC_EXT = [
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pdf",
        ".txt",
        ".odt",
        ".ods",
        ".epub",
        ".pages",
        ".pub",
        ".word",
        ".md",
        ".mdx",
        ".dot",
        ".dotx",
    ]
    VIDEO_EXT = [
        ".mp4",
        ".mov",
        ".avi",
        ".wmv",
        ".avchd",
        ".flv",
        ".f4v",
        ".swf",
        ".mkv",
        ".webm",
        ".mpeg-2",
    ]
    MUSIC_EXT = [
        ".mp3",
        ".aac",
        ".flac",
        ".alac",
        ".wav",
        ".aiff",
        ".dsd",
        ".pcm",
        ".ogg",
        ".wma",
    ]
    ZIP_EXT = [
        ".7z",
        ".gzip",
        ".zip",
        ".xz",
        ".bzip2",
        ".rar",
        ".rar5",
        ".tar",
        ".cab",
        ".lha",
        ".tgz",
    ]

    def __init__(self, location=None):
        self.location = location if location else FileOrganizer.LOCATION
        self.image_file_list = []
        self.doc_file_list = []
        self.video_file_list = []
        self.music_file_list = []
        self.zip_file_list = []
        self.other_file_list = []
        self.dir_list = []
        complete_list = listdir(self.location)
        self.make_file_list(complete_list)

    def make_file_list(self, complete_list: list):
        """Return list of files and directory based on passed list."""
        for file in complete_list:
            file_path = path.join(self.location, file)
            if path.isfile(file_path):
                file_ext = (path.splitext(file)[1]).lower()
                if file_ext in FileOrganizer.IMAGE_EXT:
                    self.image_file_list.append(file_path)
                elif file_ext in FileOrganizer.DOC_EXT:
                    self.doc_file_list.append(file_path)
                elif file_ext in FileOrganizer.VIDEO_EXT:
                    self.video_file_list.append(file_path)
                elif file_ext in FileOrganizer.MUSIC_EXT:
                    self.music_file_list.append(file_path)
                elif file_ext in FileOrganizer.ZIP_EXT:
                    self.zip_file_list.append(file_path)
                else:
                    self.other_file_list.append(file_path)
            else:
                self.dir_list.append(file_path)

    def check_directory(self, dir_location: str) -> None:
        """Check if directory exists or not. If not create one."""
        if not path.exists(dir_location):
            mkdir(dir_location)

    def file_mover(self, file_list, new_location):
        """move file based on extension list to new location."""
        for file in file_list:
            move(file, new_location)

    def organize_images(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        image_location = path.join(self.location, "Organized Images")
        self.check_directory(image_location)

        self.file_mover(self.image_file_list, image_location)

    def organize_docs(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        doc_location = path.join(self.location, "Organized Documents")
        self.check_directory(doc_location)

        self.file_mover(self.doc_file_list, doc_location)

    def organize_videos(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        video_location = path.join(self.location, "Organized Videos")
        self.check_directory(video_location)

        self.file_mover(self.video_file_list, video_location)

    def organize_music(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        music_location = path.join(self.location, "Organized Musics")
        self.check_directory(music_location)

        self.file_mover(self.music_file_list, music_location)

    def organize_zip(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        zip_location = path.join(self.location, "Organized Zip Files")
        self.check_directory(zip_location)

        self.file_mover(self.zip_file_list, zip_location)

    def organize_others(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        other_location = path.join(self.location, "Organized Other Files")
        self.check_directory(other_location)

        self.file_mover(self.other_file_list, other_location)

    def call_all(self):
        """Call all mover methods"""
        self.organize_images()
        self.organize_docs()
        self.organize_music()
        self.organize_videos()
        self.organize_zip()
        self.organize_others()


FileOrganizer().call_all()
