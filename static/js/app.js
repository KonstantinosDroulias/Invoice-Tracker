function addSupplier() {
    document.getElementById('addSupplierDiv').classList.remove('hidden');
}
function cancelSupplier() {
    document.getElementById('addSupplierDiv').classList.add('hidden');
}

function confirmDelete(btn) {
    if (confirm('Are you sure you want to delete this supplier?')) {
        btn.closest('form').submit();
    }
}