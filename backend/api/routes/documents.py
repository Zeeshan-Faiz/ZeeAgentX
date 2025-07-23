from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.api.schemas.doc_models import DocumentInfo, DeleteFileRequest
from backend.services.rag_pipeline.chroma_utils import index_document_to_chroma, delete_doc_from_chroma
from backend.utils.db_utils import insert_document_record, delete_document_record, get_all_documents
import os, shutil

router = APIRouter()

@router.post("/upload-doc")
def upload_and_index_document(file: UploadFile = File(...)):
    allowed_extensions = ['.pdf', '.docx', '.html']
    file_extension = os.path.splitext(file.filename)[1].lower()
    
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail=f"Unsupported file type. Allowed types are: {', '.join(allowed_extensions)}")
    
    temp_file_path = f"temp_{file.filename}"
    
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        file_id = insert_document_record(file.filename)
        success = index_document_to_chroma(temp_file_path, file_id)
        
        if success:
            return {"message": f"File {file.filename} successfully uploaded and indexed.", "file_id": file_id}
        else:
            delete_document_record(file_id)
            raise HTTPException(status_code=500, detail=f"Failed to index {file.filename}.")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@router.get("/list-docs", response_model=list[DocumentInfo])
def list_documents():
    return get_all_documents()

@router.post("/delete-doc")
def delete_document(request: DeleteFileRequest):
    chroma_delete_success = delete_doc_from_chroma(request.file_id)
    if chroma_delete_success:
        db_delete_success = delete_document_record(request.file_id)
        if db_delete_success:
            return {"message": f"Successfully deleted document with file_id {request.file_id}."}
        else:
            return {"error": f"Deleted from Chroma but failed in DB."}
    else:
        return {"error": f"Failed to delete from Chroma."}
